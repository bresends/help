# Tipos primitivos PostgreSQL

* __Numérico__

	* __Inteiro__
		* smallInt {2 bytes}
		* integer {4 bytes}
		* bigint {8 bytes}

	* __Real__
		* numeric 
			* Mais usado pra quantidades exatas mas é lento por ser longo
		* decimal {user specified}
		* real {4 bytes}
		* double precision {8 bytes}
		
	* __Contagem__
		* smallserial {2 bytes - autoincremento}
		* serial {4 bytes - autoincremento}
		* bigserial {2 bytes - autoincremento}

	* __Lógico__
		* boolean (true,false,null)
---

* __Data/Tempo__
	* date
	* timeStamp
	* interval
	* time
---
* __Literal__

	* __Caractere__
		* char (não usado no Posgres)
		* varchar

	* __Texto__
		* text
---

* __Espacial__
	* points
	* lines
	* line segments
	* boxes
	* paths
	* poligons
	* circles

* __Network Adress__
* __XML__
* __JSON__
* __Array__
* __Composite__
