defmodule Inverter do
  def invert(list) do
    Enum.map(list, fn (number) -> number * -1 end)
  end
end
