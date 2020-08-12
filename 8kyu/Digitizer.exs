defmodule Digitizer do
  def digitize(n) do
    String.split(String.reverse(Integer.to_string(n)), "",trim: true) |> Enum.map(&String.to_integer/1)
  end
end
