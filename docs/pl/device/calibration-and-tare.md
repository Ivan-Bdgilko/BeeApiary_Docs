# Kalibracja i tarowanie

!!! danger "Nowe urządzenie nie wymaga kalibracji"
    Kalibracja jest wymagana przede wszystkim po naprawie lub utracie fabrycznych danych kalibracyjnych. Nie używaj go jako ogólnego sposobu rozwiązywania problemów z nieprawidłowym odczytem masy.

<span id="calibration"></span>
## Kalibracja

1. Odłącz zewnętrzne zasilanie.
2. Umieść wszystkie czujniki masy na twardej, poziomej powierzchni i pozostaw platformę pustą.
3. Połącz się z punktem dostępowym urządzenia i otwórz **Ustawienia ogólne → Ustawienia wagi** w jego interfejsie internetowym.

    ![Przycisk otwierający ustawienia wagi](../../assets/en/device/calibration-and-tare/open-scale-settings.png){ .doc-screenshot }

4. Zacznij **Kalibracja zera** i poczekaj, aż zakończy się bez dotykania platformy.

    Na ekranie widoczne są dwa etapy kalibracji:

    ![etapy kalibracji wagi](../../assets/en/device/calibration-and-tare/calibration-steps.png){ .doc-screenshot }

    ![Kalibracja zera w toku](../../assets/en/device/calibration-and-tare/zero-calibration-progress.png){ .doc-screenshot }

5. Wybierz dostępny ciężar referencyjny 500, 1000 lub 5000 g i umieść go na platformie.

    ![Wybór masy referencyjnej](../../assets/en/device/calibration-and-tare/reference-weight-selection.png){ .doc-screenshot }

6. Zacznij **Kalibracja referencyjna** i poczekaj na wynik.

    ![Kalibracja odniesienia w toku](../../assets/en/device/calibration-and-tare/reference-weight-calibration-progress.png){ .doc-screenshot }

    ![wynik kalibracji wagi](../../assets/en/device/calibration-and-tare/calibration-result.png){ .doc-screenshot }

Wynik: urządzenie zapisało nowe wartości kalibracji. Sprawdź, czy wyświetlana jest masa wzorcowa.

<span id="tare"></span>
## Tara

Tarowanie pozwala pominąć masę platformy lub innej stałej konstrukcji.

1. [Połącz się z interfejsem internetowym wagi](../guides/configure-local-wifi.md).
2. Otwórz **Ustawienia ogólne → Ustawienia wagi**.
3. Wybierz sposób:

    - Jeśli znasz masę tary, wpisz ją w gramach i wybierz **Ustaw masę tary**.

        ![Wprowadzanie znanej tary](../../assets/en/device/calibration-and-tare/known-tare-weight-form.png){ .doc-screenshot }

    - Możesz też pozostawić konstrukcję na czujnikach i przyjąć bieżącą wartość jako zero.

        ![Przyjęcie aktualnej wagi jako zerowej](../../assets/en/device/calibration-and-tare/use-current-weight-as-zero.png){ .doc-screenshot }

4. Po zakończeniu sprawdź wskazanie.

Wynik: urządzenie odejmuje tarę od kolejnych pomiarów. Tarowanie nie zmienia fabrycznego współczynnika kalibracji.
