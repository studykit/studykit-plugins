# UntrimFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeatures.h>

## Description

Collection that provides access to all of the existing Untrim features in a component and supports the ability to create new Untrim features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](UntrimFeatures_add.htm) | Creates a new Untrim feature. |
| [classType](UntrimFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInputFromFaces](UntrimFeatures_createInputFromFaces.htm) | Creates an UntrimFeatureInput object that defines the input needed to create an untrim feature. Use the input object to define the input to create the desired feature and then use the Add method, passing in the UntrimFeatureInput object. |
| [createInputFromLoops](UntrimFeatures_createInputFromLoops.htm) | Creates an UntrimFeatureInput object that defines the input needed to create an untrim feature. Use the input object to define the input to create the desired feature and then use the Add method, passing in the UntrimFeatureInput object. |
| [item](UntrimFeatures_item.htm) | Function that returns the specified Untrim feature using an index into the collection. |
| [itemByName](UntrimFeatures_itemByName.htm) | Function that returns the specified Untrim feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](UntrimFeatures_count.htm) | The number of Untrim features in the collection. |
| [isValid](UntrimFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](UntrimFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.untrimFeatures](Features_untrimFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Untrim Feature API Sample](UntrimFeatureSample_Sample.htm) | Demonstrates creating a new untrim feature. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |