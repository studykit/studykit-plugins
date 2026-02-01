# InterferenceInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/InterferenceInput.h>

## Description

Used to gather and define the various inputs and settings needed to calculate interference. This object is created using the Design.createInterferenceInput method.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](InterferenceInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [areCoincidentFacesIncluded](InterferenceInput_areCoincidentFacesIncluded.htm) | Gets and sets whether any coincident faces in the input bodies are considered as interference or not. This property defaults to False for a newly created InterferenceInput object. |
| [entities](InterferenceInput_entities.htm) | Gets and set an ObjectCollection containing BRepBody and/or Occurrence entities that will be used when checking for interference. All entities must be in the context of the root component of the top-level design. |
| [isValid](InterferenceInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](InterferenceInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Design.createInterferenceInput](Design_createInterferenceInput.htm), [FlatPatternProduct.createInterferenceInput](FlatPatternProduct_createInterferenceInput.htm), [WorkingModel.createInterferenceInput](WorkingModel_createInterferenceInput.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Analyze Interference API Sample](AnalyzeInterferenceSample_Sample.htm) | Demonstrates analyzing the interference between components. This uses a direct modeling design because the ability to create bodies that represent the interference volume is only supported in a direct modeling design. |
| [Interference API Sample](InterferenceSample_Sample.htm) | Demonstrates Interference APIs. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |