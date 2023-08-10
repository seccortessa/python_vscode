; Programa para sumar los dígitos de un número y guardar el resultado en WREG

    ; Definir los registros
    cblock 0x20
    numero      ; Variable para almacenar el número
    resultado   ; Variable para almacenar el resultado de la suma
    temp        ; Variable temporal para cálculos intermedios
    endc

    ; Inicio del programa
    org 0x00

    ; Configuración e inicialización
    ; (Aquí irían las instrucciones para configurar el microcontrolador si estuvieras usando un PIC)

    ; Main loop
main_loop:
    ; Leer el número y guardarlo en el registro "numero"
    ; (Aquí irían las instrucciones para leer el número desde algún puerto o memoria)

    ; Inicializar la variable "resultado" a cero
    clrf resultado

    ; Bucle para sumar los dígitos
sum_digits:
    ; Verificar si el número es cero (fin del bucle)
    movf numero, W
    bz done

    ; Dividir el número entre 10 y obtener el residuo (dígito menos significativo)
    movlw 10
    movwf temp
    call divide_by_ten
    ; Aquí, el residuo (dígito) se encuentra en WREG

    ; Sumar el dígito al resultado
    addwf resultado, F

    ; Dividir el número entre 10 para eliminar el dígito menos significativo
    movlw 10
    movwf temp
    call divide_by_ten

    ; Repetir el bucle para sumar el siguiente dígito
    goto sum_digits

    ; Rutina para dividir el número en WREG entre el valor en "temp" y guardar el cociente en WREG
divide_by_ten:
    movwf temp       ; Guardar el divisor en "temp"
    clrf WREG        ; Limpiar WREG (cociente)
    btfsc numero, 3  ; Verificar si el bit más significativo del número está en 1
    incf WREG, F     ; Si es así, incrementar WREG (se inicia con el bit más significativo en 1)
divide_loop:
    rlf numero, F    ; Rotar el número a la izquierda (desplazar un bit hacia la izquierda)
    rlf WREG, F      ; Rotar el cociente a la izquierda
    subwf temp, F    ; Restar el divisor del número
    btfss STATUS, 0  ; Verificar el bit de carry (si es 0, el resultado fue negativo)
    goto divide_loop ; Si no hubo carry, repetir el bucle de división
    return           ; Retornar de la rutina de división

done:
    ; Aquí, el resultado de la suma se encuentra en el registro "resultado" y se puede acceder desde WREG

    ; (Aquí irían las instrucciones para realizar alguna acción con el resultado, como enviarlo por un puerto o almacenarlo en memoria)

    ; Fin del programa
    end
