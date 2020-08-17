defmodule SimpleMath do
  def basic_op(operation, value1, value2) do
    case operation do
     "+" -> value1 + value2
     "-" -> value1 - value2
     "*" -> value1 * value2
     "/" -> value1 / value2
     end
  end
end
