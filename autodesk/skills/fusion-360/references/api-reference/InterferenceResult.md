# InterferenceResult Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/InterferenceResult.h>

## Description

Represents the interference between bodies and/or occurrences in an interference analysis.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](InterferenceResult_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [entityOne](InterferenceResult_entityOne.htm) | Returns the first entity involved in the interference |
| [entityTwo](InterferenceResult_entityTwo.htm) | Returns the second entity involved in the interference |
| [interferenceBody](InterferenceResult_interferenceBody.htm) | Returns a transient BRepBody that represents the volume of interference. |
| [isCreateBody](InterferenceResult_isCreateBody.htm) | Gets and sets if this interference volume should be created as a model body. Setting this to true doesn't create the body just indicates that a body is desired. Calling the createBodies method on the interferenceResults object will result in the creation of the model body if this property is true. |
| [isValid](InterferenceResult_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](InterferenceResult_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[InterferenceResults.item](InterferenceResults_item.htm)

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |