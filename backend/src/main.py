from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.web import pedido_controller, producao_controller, tiny_controller


# Criar aplicação FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API de Gestão da Mix Shop - Controle de Produção, Separação e Expedição",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(pedido_controller.router)
app.include_router(producao_controller.router)
app.include_router(tiny_controller.router)


@app.get("/")
async def root():
    """Endpoint raiz"""
    return {
        "message": "Mix Shop API - Arquitetura Hexagonal",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "online"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )