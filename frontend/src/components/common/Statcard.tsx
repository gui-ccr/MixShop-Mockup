import React from "react";

type StatCardProps = {
    title: string;
    value: string;
    Icon: React.ElementType; // permite passa icones como prop
    colorClasses: {
        iconBg: string; // ex: "Bg-blue-400"
        iconText: string; // ex: "texte-blue-400"
    };
};

export function StatCard({title, value, Icon, colorClasses} : StatCardProps) {
    return(
        <div className="flex items-center gap-4 rounded-lg bg-white p-4 shadow-sm">
            {/* circulo do icone */}
            <div className={`rounded-full p-3 ${colorClasses.iconBg}`}>
                <Icon className={`h-6 w-6 ${colorClasses.iconText}`}/>
            </div>
            {/* conteudo de texto */}
            <div>
                <p className="text-sm text-gray-700">{title}</p>
            <p className="text-2xl font-bold text-gray-900">{value}</p>
            </div>
        </div>
    )
}