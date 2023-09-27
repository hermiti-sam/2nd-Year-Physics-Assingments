function arctan(x, N)
    pre_atan = 0
    if -1 <= x <= 1
        ex = x
    elseif 1 < x < -1
        ex = 1 / x
    end
    for n in 0:N
        pre_atan += (((-1)^n) / (2 * n + 1)) * ex^(2 * n + 1)
    end
    return pre_atan

end

print("My Function: ", arctan(1.2, 20))
print("  ")
print("Base function: ", atan(1.2))
