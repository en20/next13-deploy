"use client"
import CarouselSection from "@/components/CarouselSection";
import Footer from "@/components/Footer";
import ProtectedRoute from "@/components/ProtectedRoute";
import { NextPage } from "next";

function Home() {
  return (
    <section className="flex flex-col h-[89vh] justify-between">
      <main className="flex flex-col">
        <section className="flex flex-col w-full container-wrapper py-4">
          <h1 className="text-primary text-3xl">
            Selecione um bot
          </h1>
        </section>
        <CarouselSection />
      </main>
      <Footer/>
    </section>
  );
}

const ProtectedPage: NextPage = ProtectedRoute(Home)

export default ProtectedPage;
