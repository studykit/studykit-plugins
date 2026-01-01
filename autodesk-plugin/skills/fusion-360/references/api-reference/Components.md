# Components Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Components.h>

## Description

The Components collection object provides access to existing components in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Components_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](Components_item.htm) | Function that returns the specified component using an index into the collection. |
| [itemById](Components_itemById.htm) | Returns the Component that has the specified ID. |
| [itemByName](Components_itemByName.htm) | Function that returns the specified component by name. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](Components_count.htm) | The number of components in the collection. |
| [isValid](Components_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Components_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Design.allComponents](Design_allComponents.htm), [FlatPatternProduct.allComponents](FlatPatternProduct_allComponents.htm), [WorkingModel.allComponents](WorkingModel_allComponents.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Library Item API Sample](LibraryItemSample_Sample.htm) | Demonstrates how to examine library items using the API.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the existing default code. The script will search for and record all components and library items in the current project. They are displayed in a dialog when the script has finished. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |