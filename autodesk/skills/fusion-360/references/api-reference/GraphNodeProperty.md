# GraphNodeProperty Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/GraphNodeProperty.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Class for representing a property of a graph node. These can be of many types.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](GraphNodeProperty_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [description](GraphNodeProperty_description.htm) | Returns the description of this property. This description is localized and can change based on the current language. |
| [isValid](GraphNodeProperty_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](GraphNodeProperty_name.htm) | Gets the internal name of the property. |
| [objectType](GraphNodeProperty_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[GraphNodeProperties.item](GraphNodeProperties_item.htm), [GraphNodeProperties.itemByName](GraphNodeProperties_itemByName.htm)

## Derived Classes

[BooleanGraphNodeProperty](BooleanGraphNodeProperty.htm), [ColorControlPointMapGraphNodeProperty](ColorControlPointMapGraphNodeProperty.htm), [ColorGraphNodeProperty](ColorGraphNodeProperty.htm), [GeometryGraphNodeProperty](GeometryGraphNodeProperty.htm), [IntegerGraphNodeProperty](IntegerGraphNodeProperty.htm), [Matrix3DGraphNodeProperty](Matrix3DGraphNodeProperty.htm), [ScalarControlPointMapGraphNodeProperty](ScalarControlPointMapGraphNodeProperty.htm), [ScalarGraphNodeProperty](ScalarGraphNodeProperty.htm), [StringGraphNodeProperty](StringGraphNodeProperty.htm), [TransformRefGraphNodeProperty](TransformRefGraphNodeProperty.htm), [Vector3DGraphNodeProperty](Vector3DGraphNodeProperty.htm)

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |