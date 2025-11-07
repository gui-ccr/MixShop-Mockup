type ChipProps ={
    label: string;
    colorClasses: string;
}


export function Chip({label, colorClasses} : ChipProps){
    return(
        <span className={`inline-block rounded-full px-3 py-0.5 text-xs font-medium ${colorClasses}`}>
            {label}
        </span>
    )
}