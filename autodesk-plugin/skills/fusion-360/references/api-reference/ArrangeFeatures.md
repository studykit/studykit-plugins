# ArrangeFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeatures.h>

## Description

Provides access to the Arrange features in a component and provides the functionality to create new Arrange features

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ArrangeFeatures_add.htm) | Creates a new Arrange feature. Use the create2DInput or create3DInput method to first create an input object and fully define the required input. Then, pass that input object to the add method to create the Arrange feature. |
| [classType](ArrangeFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](ArrangeFeatures_createInput.htm) | Creates a new ArrangeFeatureInput object. An ArrangeFeatureInput object is the logical equivalent to the command dialog when creating an Arrange feature. It provides access to the various options and collects all the required input when creating an Arrange feature. Once fully defined, you pass this into the add method to create the Arrange feature. |
| [item](ArrangeFeatures_item.htm) | Returns the specified Arrange feature using an index into the collection. |
| [itemByName](ArrangeFeatures_itemByName.htm) | Returns the specified Arrange feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ArrangeFeatures_count.htm) | Returns the number of Arrange features in the component. |
| [isValid](ArrangeFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ArrangeFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.arrangeFeatures](Features_arrangeFeatures.htm)

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |