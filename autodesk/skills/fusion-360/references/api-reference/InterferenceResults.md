# InterferenceResults Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/InterferenceResults.h>

## Description

Transient object used to return the result of an interference analysis.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](InterferenceResults_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createBodies](InterferenceResults_createBodies.htm) | Creates bodies in the model that represent the interference volumes. This is not supported in parametric modeling. |
| [item](InterferenceResults_item.htm) | Function that returns the specified interference result using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](InterferenceResults_count.htm) | Returns the number of interference results in the collection. |
| [isValid](InterferenceResults_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](InterferenceResults_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Design.analyzeInterference](Design_analyzeInterference.htm), [FlatPatternProduct.analyzeInterference](FlatPatternProduct_analyzeInterference.htm), [WorkingModel.analyzeInterference](WorkingModel_analyzeInterference.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Interference API Sample](InterferenceSample_Sample.htm) | Demonstrates Interference APIs. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |