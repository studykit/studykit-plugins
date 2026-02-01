# RuledSurfaceFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeatures.h>

## Description

Collection that provides access to all of the existing Ruled Surface features in a component and supports the ability to create new Ruled Surface features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](RuledSurfaceFeatures_add.htm) | Creates a new RuledSurface feature. |
| [classType](RuledSurfaceFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](RuledSurfaceFeatures_createInput.htm) | Creates a RuledSurfaceFeatureInput object that defines the input needed to create a ruled surface feature. Use the input object to define the input to create the desired feature and then use the Add method, passing in the RuledSurfaceFeatureInput object. |
| [item](RuledSurfaceFeatures_item.htm) | Function that returns the specified ruled surface feature using an index into the collection. |
| [itemByName](RuledSurfaceFeatures_itemByName.htm) | Function that returns the specified RuledSurface feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](RuledSurfaceFeatures_count.htm) | The number of RuledSurface features in the collection. |
| [isValid](RuledSurfaceFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](RuledSurfaceFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.ruledSurfaceFeatures](Features_ruledSurfaceFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Ruled Surface Feature API Sample](RuledSurfaceFeatureSample_Sample.htm) | Demonstrates creating a new ruled surface feature. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |