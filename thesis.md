# 1. Introduzione

#### 1.1 Robot di servizio

I robot di servizio sono una tipologia di robot creata per assistere l'essere umano in ambienti antropocentrici, come abitazioni, uffici e ospedali, il tutto in maniera autonoma o semi-autonoma. L'obiettivo è semplificare la vita quotidiana delle persone, aumentando la sicurezza e la produttività.

Negli ultimi decenni questi robot si sono diffusi in vari settori, come quello logistico e sanitario, andando a supportare attività potenzialmente pericolose e soggette ad errori, come ad esempio il trasporto di carichi pesanti o la consegna di medicinali e materiale medico.

Il motivo della diffusione dei robot per questi specifici compiti risiede nel tipo di ambiente nel quale operano; un magazzino è un ambiente totalmente prevedibile, in quanto ogni robot mobile conosce lo stato e la posizione di ogni singolo prodotto sulle scaffalature, così come la posizione di ogni altro robot all'interno della struttura. La stessa cosa non si può invece dire nel caso di ambienti più complessi, come ad esempio quello domestico. In ogni abitazione caratteristiche come la planimetria e l'arredamento possono cambiare totalmente, oltre agli ostacoli presenti, siano essi mobili o fissi. A tutto questo si aggiungono anche i comportamenti imprevedibili di persone e animali, che possono interferire con le attività del robot [[1]](https://ieeexplore.ieee.org/abstract/document/6301139).

Un robot di servizio deve quindi riuscire a percepire e comprendere l'ambiente che lo circonda, così da poter svolgere compiti essenziali come la localizzazione, la navigazione, e la pianificazione. Questo è possibile grazie a telecamere e sensori di profondità, che consentono di acquisire immagini e mappare lo spazio circostante, e a reti neurali che permettono di riconoscere e classificare oggetti. L'insieme di queste tecniche è comunemente chiamato robotic vision.

###### 1.1.1 Problema della raccolta dati

L'addestramento di reti neurali è uno dei processi più importanti nella creazione di un sistema di robotic vision, e il suo corretto funzionamento dipende da vari fattori come la scelta del modello e dal processo di raccolta dei dati.

Per quanto riguarda la selezione del modello, a seconda delle attività che il robot deve svolgere si preferiscono determinate tipologie di modelli ad altre. Ad esempio, se si vogliono riconoscere oggetti in tempo reale si preferiranno reti neurali di tipo convoluzionale [[2]](https://arxiv.org/abs/1511.08458) (CNN, Convolutional Neural Network), mentre se l'obiettivo è comprendere sequenze di azioni complesse, come nel caso dell'interazione con gli esseri umani, si opterà per reti neurali ricorrenti [[3]](https://arxiv.org/abs/1801.01078) (RNN, Recurrent Neural Network). La sfida più grande non è però la scelta del modello, quanto la raccolta dei dati utilizzata per l'addestramento.

Raccogliere dati è da sempre un processo complesso in qualsiasi ambito, ma trova maggiori difficoltà in progetti di robotic vision. In questi casi, infatti, i dati vengono acquisiti facendo interagire robot con ambienti del mondo reale. Questo approccio ha però diverse limitazioni, dovute a fattori come il tempo e i costi che la raccolta comporta.
