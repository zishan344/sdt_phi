export interface childrenProps {
  children: React.ReactNode;
}
export interface ProductData {
  name: string;
  description?: string | null;
  price: number;
  stock: number;
  category: number;
}

interface ProductImage {
  id: number;
  image: string;
}

export interface ProductDetails {
  id?: number;
  name: string;
  description?: string | null;
  price: number;
  stock: number;
  category: number;
  price_with_tax?: string;
  images?: ProductImage[];
}
