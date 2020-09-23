**comentarios ejercicios W8**

**height_weight.ipynb**

Este ejercicio está bien, aunque no me queda claro que hayas entendido bien el ejercicio. Al final has aplicado el código que dio Gabriel con el fin de mostrar un gráfico con los errors. 

Si el entrenamiento de un modelo se pudiera resumir en unos puntos serían los siguientes:

1. Dividir el dataset: X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
2. Asignar el modelo: lin_reg = LinearRegression()
3. Entrenar el modelo: lin_reg.fit(X_train, y_train)
4. Predecir con el modelo: ling_reg.predict(X_test)

Prueba a resolver este ejercicio siguiendo estos pasos.
Cuando lo hayas hecho, prueba a multiplicar cada columna por 2 y ver si cambia el score. 

**houses.ipynb**

En este ejercicio, veo que hay mucho código, código que además repites, el algoritmo LinearRegressor() se asigna hasta a 3 variables diferentes: lm, lin_reg, new_model, y a estos varias veces. 

Acostúmbrate a importar las librerías en la primera celda, por dos motivos:
- evitar importar la misma librería varias veces
- mantener un orden

Lo mismo te digo para el resto del código, si sigues el orden que te comentaba para el ejercicio anterior deberías poder resolver este ejercicio sin más dificultad.
En este caso el punto 4 de los puntos que comenté en el otro ejercicio, pasa a hacerse dentro de la función `plot`. 

4.  plt.scatter(X, y, color='b')
    plt.plot(X, lin_reg.predict(X), color='red')
    plt.title(elem)
    plt.show()

De hecho, como comentamos en clase con Jose Luis, podías hacer un `for` a una lista de las columnas y por cada una de ellas sacar un gráfico de los puntos y una línea con la predicción del modelo. 

```python
for col in housing.columns.tolist():
    X = housing[col]
    #resto del código (paso 1,2,3,4)
```

¡Pruébalo y me dices!


**1.multinominal_regression.ipynb**

En este ejercicio realmente hay código que no tiene mucha relación entre sí, de hecho he intentado ejecutarlo y me daba errores por todas partes...

Sobretodo el problema de este ejercicio es un problema de regresión y por tanto, no es adecuado que uses el algoritmo LogisticRegressor() ya que este es de clasificación a pesar de su nombre. Por este motivo te da uno de los errores, ValueError: Unknown label type: 'continuous'.
https://stackoverflow.com/questions/41925157/logisticregression-unknown-label-type-continuous-using-sklearn-in-python

En este caso, debías resolver este ejercicio usando LinearRegression() que aunque no va a darte un score bueno porque no se ajusta bien a los datos, al menos te va a dejar seguir los pasos 1-4 ;) 

PD: Muy guay los pairplot :) 

**2.log_regresion_exercise.ipynb**

En general, mucho mejor este ejercicio, de hecho salvo cuando vas a hacer la predicción está perfecto. 

Cuando vas a hacer la predicción el error está en darle un diccionario en vez de un array, que es lo que conoce el modelo.

Piensa que en vez de X_test, ahora le estás dando un X_new pero que debería tener el  mismo "aspecto" y forma. 

`predicted = model.predict([[15.7,2.8,9.5,0.1]])`

El otro error que tienes en el archivo es porque estás intentando codificar un dataframe entero, cuando `fit_transform` trabaja con arrays tal que así según se lee en la documentación de LabelEncoder():

fit_transform(y)
Fit label encoder and return encoded labels

Parameters
yarray-like of shape 
Target values.

Returns
yarray-like of shape 

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.fit_transform



¡Toma nota de estos puntos y keep coding! :D 