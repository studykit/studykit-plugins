# ModifyUtility Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/ModifyUtility/ModifyUtility.h>

## Description

Base class for all modify utilities.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ModifyUtility_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ModifyUtility_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ModifyUtility_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAMAdditiveContainer.modifyUtility](CAMAdditiveContainer_modifyUtility.htm), [CAMFolder.modifyUtility](CAMFolder_modifyUtility.htm), [CAMHoleRecognition.modifyUtility](CAMHoleRecognition_modifyUtility.htm), [CAMPattern.modifyUtility](CAMPattern_modifyUtility.htm), [NCProgram.modifyUtility](NCProgram_modifyUtility.htm), [Operation.modifyUtility](Operation_modifyUtility.htm), [OperationBase.modifyUtility](OperationBase_modifyUtility.htm), [Setup.modifyUtility](Setup_modifyUtility.htm)

## Derived Classes

[AdditiveSetupUtility](AdditiveSetupUtility.htm)

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |