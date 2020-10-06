export function abbrevName(name: string): string {
    return name.split(" ").map(n=>n[0].toUpperCase()).join(".");
}
