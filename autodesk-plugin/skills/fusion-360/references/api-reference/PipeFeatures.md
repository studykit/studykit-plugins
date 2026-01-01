# PipeFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeatures.h>

## Description

Collection that provides access to all of the existing Pipe features in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](PipeFeatures_add.htm) | Creates a new Pipe feature. |
| [classType](PipeFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](PipeFeatures_createInput.htm) | Creates a PipeFeatureInput object for defining a simple Pipe feature with only a path. Use properties and methods on this object to define the Pipe you want to create and then use the Add method, passing in the PipeFeatureInput object. |
| [item](PipeFeatures_item.htm) | Function that returns the specified Pipe feature using an index into the collection. |
| [itemByName](PipeFeatures_itemByName.htm) | Function that returns the specified Pipe feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](PipeFeatures_count.htm) | The number of Pipe features in the collection. |
| [isValid](PipeFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](PipeFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.pipeFeatures](Features_pipeFeatures.htm)

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |