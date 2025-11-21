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
