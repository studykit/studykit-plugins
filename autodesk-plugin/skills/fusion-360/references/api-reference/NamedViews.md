# NamedViews Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/NamedViews.h>

## Description

Collection that provides access to all of the existing named views associated with a Product and supports the creation of new named views.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](NamedViews_add.htm) | Creates a new named view. |
| [classType](NamedViews_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](NamedViews_item.htm) | Returns the specified named view using an index into the collection. The four standard named views ("TOP", "FRONT", "RIGHT", and "HOME") are not accessible through this method. For the predefined view use the properties on this collection that provide direct access to the specific named view. |
| [itemByName](NamedViews_itemByName.htm) | Returns the specified named view using the name of the named view. The four standard named views ("TOP", "FRONT", "RIGHT", and "HOME") are not accessible through this method. For the predefined view use the properties on this collection that provide direct access to the specific named view. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](NamedViews_count.htm) | Returns the number of named views associated with the product. The four standard named views ("TOP", "FRONT", "RIGHT", and "HOME") are not included in this count. Only user-created named view are counted. |
| [frontNamedView](NamedViews_frontNamedView.htm) | Returns the standard named view called "FRONT". |
| [homeNamedView](NamedViews_homeNamedView.htm) | Returns the standard named view called "HOME". |
| [isValid](NamedViews_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](NamedViews_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [rightNamedView](NamedViews_rightNamedView.htm) | Returns the standard named view called "RIGHT". |
| [topNamedView](NamedViews_topNamedView.htm) | Returns the standard named view called "TOP". |

## Accessed From

[CAM.namedViews](CAM_namedViews.htm), [Design.namedViews](Design_namedViews.htm), [Drawing.namedViews](Drawing_namedViews.htm), [FlatPatternProduct.namedViews](FlatPatternProduct_namedViews.htm), [Product.namedViews](Product_namedViews.htm), [WorkingModel.namedViews](WorkingModel_namedViews.htm)

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |