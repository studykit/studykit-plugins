# ExtrudeFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatures.h>

## Description

Collection that provides access to all of the existing extrude features in a design and supports the ability to create new extrude features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ExtrudeFeatures_add.htm) | Creates a new extrude feature based on the information defined by the provided ExtrudeFeatureInput object. To create a new extrusion use the createInput function to create a new input object and use the methods and properties on that object to define the required input for an extrusion. Once the information is defined on the input object you can pass it to the Add method to create the extrusion. |
| [addSimple](ExtrudeFeatures_addSimple.htm) | Creates a basic extrusion that goes from the profile plane the specified distance. |
| [classType](ExtrudeFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](ExtrudeFeatures_createInput.htm) | Creates a new ExtrudeFeatureInput object that is used to specify the input needed to create a new extrude feature. |
| [item](ExtrudeFeatures_item.htm) | Function that returns the specified extrude feature using an index into the collection. |
| [itemByName](ExtrudeFeatures_itemByName.htm) | Function that returns the specified extrude feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ExtrudeFeatures_count.htm) | The number of extrude features in the collection. |
| [isValid](ExtrudeFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ExtrudeFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.extrudeFeatures](Features_extrudeFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |
| [Move Feature API Sample](MoveFeatureSample_Sample.htm) | Demonstrates creating a new move feature. |
| [Manage Participant Bodies API Sample](ParticipantBodiesSample_Sample.htm) | Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |
| [ReplaceFace Feature](ReplaceFaceFeatureSample_Sample.htm) | Demonstrates creating a new replaceface feature. |
| [Shell Feature API Sample](ShellFeatureSample_Sample.htm) | Demonstrates creating a new shell feature. |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |