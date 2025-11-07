export type Pedido = {
  id: number;
  sku: string;
  codigo: string;
  descricao: string;
  status:
    | "Pendente"
    | "Imprimindo"
    | "Parcial"
    | "Concluído"
    | "Embalado"
    | "Enviado";
};

export const mockPedidos: Pedido[] = [
  {
    id: 1,
    sku: "MIX-TSH-001-P",
    codigo: "1001",
    descricao: "Camiseta Lisa Preta -P",
    status: "Pendente",
  },
  {
    id: 2,
    sku: "MIX-CAN-002-G",
    codigo: "1002",
    descricao: "Caneca Branca -G",
    status: "Imprimindo",
  },
  {
    id: 3,
    sku: "MIX-TSH-003-M",
    codigo: "1003",
    descricao: "Camiseta Lisa Branca -M",
    status: "Concluído",
  },
  {
    id: 4,
    sku: "MIX-CAN-004-P",
    codigo: "1004",
    descricao: "Caneca Harry Potter -P",
    status: "Embalado",
  },
  {
    id: 5,
    sku: "MIX-COP-009-M",
    codigo: "1005",
    descricao: "Copo de League Of Legends",
    status: "Enviado",
  },
  {
    id: 6,
    sku: "MIX-TGR-004",
    codigo: "1006",
    descricao: "Teclado Gamer RGB",
    status: "Parcial",
  },
];
