"use client";

import { jwtDecode } from "jwt-decode";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function Page() {
  const router = useRouter();

  const token = localStorage.getItem("token");

  useEffect(() => {
    if (!token) {
      router.push("/login");
      return;
    }
  }, [router, token]);

  const decoded_token = token ? jwtDecode(token) : "No token.";
  return (
    <div className="h-full">
      <div className="m-auto block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
        <p className="font-normal text-gray-700 dark:text-gray-400">
          {JSON.stringify(decoded_token)}
        </p>
      </div>
    </div>
  );
}
