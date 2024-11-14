# 1. Introduzione

#### 1.1 Robot di servizio

I robot di servizio sono una tipologia di robot creata per assistere l'essere umano in ambienti antropocentrici, come abitazioni, uffici e ospedali, il tutto in maniera autonoma o semi-autonoma. L'obiettivo è semplificare la vita quotidiana delle persone, aumentando la sicurezza e la produttività.

Negli ultimi decenni questi robot si sono diffusi in vari settori, come quello logistico e sanitario, andando a supportare attività potenzialmente pericolose e soggette ad errori, come ad esempio il trasporto di carichi pesanti o la consegna di medicinali e materiale medico.

Il motivo della diffusione dei robot per questi specifici compiti risiede nel tipo di ambiente nel quale operano; un magazzino è un ambiente totalmente prevedibile, in quanto ogni robot mobile conosce lo stato e la posizione di ogni singolo prodotto sulle scaffalature, così come la posizione di ogni altro robot all'interno della struttura. La stessa cosa non si può invece dire nel caso di ambienti più complessi, come ad esempio quello domestico. In ogni abitazione caratteristiche come la planimetria e l'arredamento possono cambiare totalmente, oltre agli ostacoli presenti, siano essi mobili o fissi. A tutto questo si aggiungono anche i comportamenti imprevedibili di persone e animali, che possono interferire con le attività del robot [[1]](https://ieeexplore.ieee.org/abstract/document/6301139).

Un robot di servizio deve quindi riuscire a percepire e comprendere l'ambiente che lo circonda, così da poter svolgere compiti essenziali come la localizzazione, la navigazione e la pianificazione. Questo è possibile grazie a telecamere e sensori di profondità, che consentono di acquisire immagini e mappare lo spazio circostante, e a reti neurali che permettono di riconoscere e classificare oggetti. L'insieme di queste tecniche è comunemente chiamata robotic vision.

#### 1.2 Problema della raccolta dati

L'addestramento di reti neurali è uno dei processi più importanti nella creazione di un sistema di robotic vision, e il suo corretto funzionamento dipende da vari fattori come la scelta del modello e dal processo di raccolta dei dati.

Per quanto riguarda la selezione del modello, a seconda delle attività che il robot deve svolgere si preferiscono determinate tipologie di modelli ad altre. Ad esempio, se si vogliono riconoscere oggetti in tempo reale si preferiranno reti neurali di tipo convoluzionale [[2]](https://arxiv.org/abs/1511.08458) (CNN, Convolutional Neural Network), mentre se l'obiettivo è comprendere sequenze di azioni complesse, come nel caso dell'interazione con gli esseri umani, si opterà per reti neurali ricorrenti [[3]](https://www.sciencedirect.com/science/article/pii/S0007850620300998) (RNN, Recurrent Neural Network). La sfida più grande non è però la scelta del modello, quanto la raccolta dei dati utilizzata per l'addestramento.

Raccogliere dati è da sempre un processo complesso in qualsiasi ambito, ma trova maggiori difficoltà in progetti di robotic vision. In questi casi, infatti, i dati vengono generalmente acquisiti facendo interagire robot con ambienti del mondo reale. Questo approccio ha però diverse limitazioni, dovute a fattori come il tempo e i costi che la raccolta comporta, oltre che per motivi riguardanti la sicurezza di persone, animali e oggetti presenti nell'ambiente. A questi elementi si aggiunge anche il fattore riproducibilità, che viene meno quando si hanno variazioni nell'hardware utilizzato o negli ambienti considerati, e che può condurre a risultati differenti. 

#### 1.3 Addestramento con dati simulati

Una possibile soluzione a questi problemi è l'utilizzo di ambienti simulati per la raccolta di dati. Questo permette infatti di ottenere dati a basso costo, in quanto non è necessario impegnare veri ambienti e robot, in tempi più brevi, grazie al fatto che le simulazioni possono essere velocizzate o parallelizzate, e senza i possibili rischi che una reale interazione con l'ambiente comporta.

Un simulatore consente inoltre di conoscere in anticipo e progettare gli scenari in cui un robot andrà ad interagire, andando a regolare vari parametri così da controllarne ogni singolo aspetto. Questo garantisce che l'ambiente non vari ed evolva nel tempo, a meno che non sia stato appositamente programmato per farlo.

Questo approccio permette di risolvere molti problemi, ma ne introduce di nuovi. La simulazione è infatti solo un'approssimazione della realtà, e non è possibile replicare fedelmente tutti i fenomeni e le caratteristiche del mondo reale. I motivi per i quale queste tipologie di ambienti differiscono sono principalmente due: il fotorealismo e l'interazione fisica.

Per fotorealismo si intende la capacità del simulatore di riprodurre in maniera visivamente accurata ambienti reali, in modo dettagliato e credibile. Tuttavia, risulta difficile replicare fenomeni come l'illuminazione, le riflessioni e texture di superfici. Questa mancanza di dettaglii ha un grande impatto sulla qualità dei dati raccolti per l'addestramento, con una conseguente mancanza di generalizzazione nel mondo reale da parte del modello. Una soluzione che permette di mitigare questo problema è l'adozione di una tecnica chiamata domain randomization [[4]](https://ieeexplore.ieee.org/abstract/document/8202133), che permette di variare caratteristiche ed oggetti presenti nell'ambiente simulato (posizione e tipi di oggetti, illuminazione, texture). Questo permette di rendere il modello più robusto, permettendogli di operare meglio in contesti reali.

L'interazione fisica si riferisce invece all'abilità del simulatore di riuscire a replicare le leggi della fisica in maniera realistica; questo comprende ad esempio il movimento e l'interazione tra oggetti. 

In questi ultimi anni sono stati sviluppati diversi nuovi simulatori [[5]](https://arxiv.org/abs/1712.05474) [[6]](https://proceedings.neurips.cc/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html) [[7]](https://arxiv.org/abs/1908.01887) [[8]](https://ieeexplore.ieee.org/abstract/document/1389727), ognuno specializzato per specifici casi d'uso, e tutti si concentrano pervalentemente su uno dei due aspetti sopra citati.

#### 1.4 Problema del sim to real gap

Reti neurali addestrate con dati provenienti da simulatori e testati negli stessi ambienti simulati, otterranno risultati eccellenti. Sapranno infatti individuare e riconoscere correttamente gli oggetti presenti. Questo perchè il dominio dei dati utilizzato per l'addestramento e quello usato per il testing è lo stesso. Invece, l'adozione di reti naurali addestrare con dati sintetici in ambienti reali, avranno performance scadenti, non riuscendo neanche a riconoscere le categorie di oggetti più comuni presenti nel mondo reale [[9]](https://ieeexplore.ieee.org/abstract/document/8793591). Questo problema è noto come sim to real gap, letteralmente 'divario tra simulazione e realtà'.
