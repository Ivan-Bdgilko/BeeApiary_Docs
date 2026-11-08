/* Estimates are based on the documented operating model; currents are in mA. */
(() => {
  const strings = {
    uk: ['Калькулятор автономності', 'Ревізія плати', '2023 — сон 65 мкА', '2026 — сон 0,145 мкА', 'Ємність батареї', 'Базова — 1,8 А·год', 'Підсилена — 3,6 А·год', 'Підсилена — 4,2 А·год', 'Канал зв’язку', 'Передавань на добу', 'Тривалість сеансу з радіо', 'с', 'Споживання за добу', 'мА·год', 'Розрахункова автономність', 'днів', 'місяців', '24 пробудження на добу: вимірювання без радіо — 5 с; сеанс із радіо вже включає вимірювання. microSD і датчик ваги працюють протягом кожного пробудження.', 'Розрахунок показує приблизний час роботи за обраних налаштувань.'],
    en: ['Battery life calculator', 'Board revision', '2023 — sleep 65 µA', '2026 — sleep 0.145 µA', 'Battery capacity', 'Standard — 1.8 Ah', 'Extended — 3.6 Ah', 'Extended — 4.2 Ah', 'Communication channel', 'Transmissions per day', 'Radio session duration', 's', 'Daily consumption', 'mAh', 'Estimated battery life', 'days', 'months', '24 wake-ups per day: measurements without radio take 5 s; radio sessions include measurement. The microSD and load sensor are powered throughout each wake-up.', 'The calculation shows the approximate battery life for the selected settings.'],
    de: ['Laufzeitrechner', 'Platinenrevision', '2023 — Schlafmodus 65 µA', '2026 — Schlafmodus 0,145 µA', 'Akkukapazität', 'Standard — 1,8 Ah', 'Erweitert — 3,6 Ah', 'Erweitert — 4,2 Ah', 'Übertragungsweg', 'Übertragungen pro Tag', 'Dauer einer Funksitzung', 's', 'Verbrauch pro Tag', 'mAh', 'Geschätzte Laufzeit', 'Tage', 'Monate', '24 Aufwachvorgänge pro Tag: Eine Messung ohne Funk dauert 5 s; die Funksitzung enthält bereits die Messung. microSD und Gewichtssensor sind während jedes Aufwachvorgangs aktiv.', 'Die Berechnung zeigt die ungefähre Laufzeit für die gewählten Einstellungen.'],
    es: ['Calculadora de autonomía', 'Revisión de la placa', '2023 — reposo 65 µA', '2026 — reposo 0,145 µA', 'Capacidad de la batería', 'Básica — 1,8 Ah', 'Ampliada — 3,6 Ah', 'Ampliada — 4,2 Ah', 'Canal de comunicación', 'Transmisiones por día', 'Duración de la sesión de radio', 's', 'Consumo diario', 'mAh', 'Autonomía estimada', 'días', 'meses', '24 activaciones al día: cada medición sin radio dura 5 s; la sesión de radio incluye la medición. La microSD y el sensor de peso funcionan durante cada activación.', 'El cálculo muestra la autonomía aproximada con los ajustes seleccionados.'],
    fr: ['Calculateur d’autonomie', 'Révision de la carte', '2023 — veille 65 µA', '2026 — veille 0,145 µA', 'Capacité de la batterie', 'Standard — 1,8 Ah', 'Renforcée — 3,6 Ah', 'Renforcée — 4,2 Ah', 'Canal de communication', 'Transmissions par jour', 'Durée de la session radio', 's', 'Consommation quotidienne', 'mAh', 'Autonomie estimée', 'jours', 'mois', '24 réveils par jour : une mesure sans radio dure 5 s ; la session radio comprend la mesure. La microSD et le capteur de poids restent alimentés à chaque réveil.', 'Le calcul indique l’autonomie approximative avec les paramètres sélectionnés.'],
    pl: ['Kalkulator czasu pracy', 'Wersja płyty', '2023 — uśpienie 65 µA', '2026 — uśpienie 0,145 µA', 'Pojemność akumulatora', 'Podstawowa — 1,8 Ah', 'Powiększona — 3,6 Ah', 'Powiększona — 4,2 Ah', 'Kanał łączności', 'Transmisje na dobę', 'Czas sesji radiowej', 's', 'Zużycie na dobę', 'mAh', 'Szacowany czas pracy', 'dni', 'miesięcy', '24 wybudzenia na dobę: pomiar bez radia trwa 5 s; sesja radiowa obejmuje pomiar. Karta microSD i czujnik masy są zasilane przez cały czas każdego wybudzenia.', 'Obliczenie pokazuje przybliżony czas pracy dla wybranych ustawień.'],
    'pt-BR': ['Calculadora de autonomia', 'Revisão da placa', '2023 — repouso 65 µA', '2026 — repouso 0,145 µA', 'Capacidade da bateria', 'Básica — 1,8 Ah', 'Ampliada — 3,6 Ah', 'Ampliada — 4,2 Ah', 'Canal de comunicação', 'Transmissões por dia', 'Duração da sessão de rádio', 's', 'Consumo diário', 'mAh', 'Autonomia estimada', 'dias', 'meses', '24 ativações por dia: uma medição sem rádio dura 5 s; a sessão de rádio inclui a medição. O microSD e o sensor de peso ficam alimentados durante cada ativação.', 'O cálculo mostra a autonomia aproximada para as configurações selecionadas.'],
    tr: ['Pil ömrü hesaplayıcısı', 'Kart sürümü', '2023 — uyku 65 µA', '2026 — uyku 0,145 µA', 'Pil kapasitesi', 'Temel — 1,8 Ah', 'Güçlendirilmiş — 3,6 Ah', 'Güçlendirilmiş — 4,2 Ah', 'İletişim kanalı', 'Günlük aktarım sayısı', 'Radyo oturumu süresi', 'sn', 'Günlük tüketim', 'mAh', 'Tahmini pil ömrü', 'gün', 'ay', 'Günde 24 uyanma: radyo olmadan ölçüm 5 sn sürer; radyo oturumu ölçümü içerir. microSD ve ağırlık sensörü her uyanma boyunca güç alır.', 'Hesaplama, seçilen ayarlar için yaklaşık çalışma süresini gösterir.']
  };
  const sessionLabels = {
    uk: 'Сеансів зв’язку на добу',
    en: 'Communication sessions per day',
    de: 'Kommunikationssitzungen pro Tag',
    es: 'Sesiones de comunicación al día',
    fr: 'Sessions de communication par jour',
    pl: 'Sesje łączności na dobę',
    'pt-BR': 'Sessões de comunicação por dia',
    tr: 'Günlük iletişim oturumu sayısı'
  };
  const simLabels = {
    uk: ['Кількість номерів', 'На один номер', 'На два номери', 'Слабкий сигнал'],
    en: ['Number of phone numbers', 'One number', 'Two numbers', 'Weak signal'],
    de: ['Anzahl der Telefonnummern', 'Eine Nummer', 'Zwei Nummern', 'Schwaches Signal'],
    es: ['Cantidad de números', 'Un número', 'Dos números', 'Señal débil'],
    fr: ['Nombre de numéros', 'Un numéro', 'Deux numéros', 'Signal faible'],
    pl: ['Liczba numerów', 'Jeden numer', 'Dwa numery', 'Słaby sygnał'],
    'pt-BR': ['Quantidade de números', 'Um número', 'Dois números', 'Sinal fraco'],
    tr: ['Telefon numarası sayısı', 'Bir numara', 'İki numara', 'Zayıf sinyal']
  };
  const perDay = {
    uk: 'добу', en: 'day', de: 'Tag', es: 'día',
    fr: 'jour', pl: 'dobę', 'pt-BR': 'dia', tr: 'gün'
  };
  const simButtons = {
    uk: ['1 номер', '2 номери'], en: ['1 number', '2 numbers'],
    de: ['1 Nummer', '2 Nummern'], es: ['1 número', '2 números'],
    fr: ['1 numéro', '2 numéros'], pl: ['1 numer', '2 numery'],
    'pt-BR': ['1 número', '2 números'], tr: ['1 numara', '2 numara']
  };

  function calculate(sleep, capacity, channel, count, seconds) {
    const measurementTime_sec = 5;
    const measurementTime = (24 - count) * measurementTime_sec;
    const radioTime = count * seconds;
    const activeTime = radioTime;
    const sleepTime = 86400 - activeTime;
    const daily = (sleep * sleepTime + 50 * measurementTime + channel * radioTime + (4.56 + 3.56) * activeTime) / 3600;
    return { daily, days: capacity * 0.8 / daily, activeTime, sleepTime };
  }

  function formatDuration(days, locale) {
    const totalDays = Math.round(days);
    const months = Math.floor(totalDays / 30.44);
    const remainingDays = Math.round(totalDays - months * 30.44);
    const formatUnit = (value, unit, unitDisplay, maximumFractionDigits = 0) =>
      new Intl.NumberFormat(locale, { style: 'unit', unit, unitDisplay, maximumFractionDigits }).format(value);
    const formatDays = (value) => {
      if (!locale.toLowerCase().startsWith('uk')) return formatUnit(value, 'day', 'long');
      const form = new Intl.PluralRules('uk').select(value);
      return `${new Intl.NumberFormat(locale).format(value)} ${{ one: 'доба', few: 'доби', many: 'діб', other: 'доби' }[form]}`;
    };
    return {
      years: `≈ ${formatUnit(days / 365.25, 'year', 'long', 1)}`,
      months: `${formatUnit(months, 'month', 'short')} ${formatDays(remainingDays)}`,
      days: formatDays(totalDays)
    };
  }

  function initialize() {
    const locale = document.documentElement.lang || 'uk';
    const key = Object.keys(strings).find((language) => language.toLowerCase() === locale.toLowerCase());
    const t = strings[key] || (locale.toLowerCase() === 'pt' ? strings['pt-BR'] : strings[locale.split('-')[0].toLowerCase()]) || strings.uk;
    const sessionLabel = sessionLabels[key] || (locale.toLowerCase() === 'pt' ? sessionLabels['pt-BR'] : sessionLabels.uk);
    const sim = simLabels[key] || (locale.toLowerCase() === 'pt' ? simLabels['pt-BR'] : simLabels.uk);
    const simChoices = simButtons[key] || (locale.toLowerCase() === 'pt' ? simButtons['pt-BR'] : simButtons.uk);
    const dayUnit = perDay[key] || (locale.toLowerCase() === 'pt' ? perDay['pt-BR'] : perDay.uk);
    const number = new Intl.NumberFormat(locale, { maximumFractionDigits: 2 });
    document.querySelectorAll('.battery-calculator:not([data-initialized])').forEach((root, index) => {
      root.dataset.initialized = 'true';
      const id = `battery-calculator-${index}`;
      root.innerHTML = `<h3>${t[0]}</h3>
        <fieldset class="battery-calculator__choice"><legend>${t[8]}</legend><div class="battery-calculator__segments">
          <label><input type="radio" name="${id}-channel" value="110"><span>BLE</span></label>
          <label><input type="radio" name="${id}-channel" value="180"><span>Wi-Fi</span></label>
          <label><input type="radio" name="${id}-channel" value="230" checked><span>SIM800</span></label>
        </div></fieldset>
        <fieldset class="battery-calculator__choice"><legend>${t[1]}</legend><div class="battery-calculator__segments">
          <label><input type="radio" name="${id}-board" value="0.065" checked><span>rev 2023</span></label>
          <label><input type="radio" name="${id}-board" value="0.000145"><span>rev 2026</span></label>
        </div></fieldset>
        <fieldset class="battery-calculator__choice"><legend>${t[4]}</legend><div class="battery-calculator__segments">
          <label><input type="radio" name="${id}-battery" value="3200" checked><span>${number.format(3.2)} ${locale.toLowerCase().startsWith('uk') ? 'А·год' : 'Ah'}</span></label>
          <label><input type="radio" name="${id}-battery" value="6400"><span>${number.format(6.4)} ${locale.toLowerCase().startsWith('uk') ? 'А·год' : 'Ah'}</span></label>
        </div></fieldset>
        <fieldset class="battery-calculator__choice"><legend>${sessionLabel}</legend><div id="${id}-counts" class="battery-calculator__segments"></div></fieldset>
        <fieldset class="battery-calculator__choice"><legend id="${id}-seconds-label"></legend><div id="${id}-durations" class="battery-calculator__segments"></div></fieldset>
        <label id="${id}-weak-label"><input id="${id}-weak" type="checkbox"> ${sim[3]}</label>
        <div class="battery-calculator__results" aria-live="polite"><div>${t[14]}<strong id="${id}-years"></strong><span id="${id}-days"></span></div></div>
        <p>${t[18]}</p>`;
      const get = (name) => root.querySelector(`#${id}-${name}`);
      let previousChannel = null;
      const buttons = (name, choices, initial) => choices.map(([value, label]) =>
        `<label><input type="radio" name="${id}-${name}" value="${value}"${value === initial ? ' checked' : ''}><span>${label}</span></label>`).join('');
      const update = () => {
        const selected = (name) => Number(root.querySelector(`input[name="${id}-${name}"]:checked`).value);
        const channel = selected('channel');
        const isSim = channel === 230;
        if (channel !== previousChannel) {
          const counts = channel === 110 ? [8, 12, 16] : [2, 3, 4, 6, 8];
          const durations = isSim ? [[20, simChoices[0]], [35, simChoices[1]]] :
            (channel === 110 ? [15, 30, 45, 60] : [30, 45, 60]).map(value => [value, `${value} ${t[11]}`]);
          get('counts').innerHTML = buttons('count', counts.map(value => [value, number.format(value)]), channel === 110 ? 8 : 4);
          get('durations').innerHTML = buttons('seconds', durations, isSim ? 20 : 30);
          if (!isSim) get('weak').checked = false;
          previousChannel = channel;
        }
        get('weak-label').hidden = !isSim;
        get('seconds-label').textContent = isSim ? sim[0] : t[10];
        const count = selected('count');
        const seconds = selected('seconds') * (isSim && get('weak').checked ? 2 : 1);
        const result = calculate(selected('board'), selected('battery'), channel, count, seconds);
        const duration = formatDuration(result.days, locale);
        get('years').textContent = `${duration.years} (${duration.months})`;
        get('days').textContent = `${duration.days} (${number.format(result.daily)} ${t[13]}/${dayUnit})`;
      };
      root.addEventListener('input', update);
      root.addEventListener('change', update);
      update();
    });
  }
  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialize);
    else initialize();
  }
  if (typeof module !== 'undefined') module.exports = { calculate, formatDuration };
})();
