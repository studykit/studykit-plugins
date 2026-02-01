# NamedView Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/NamedView.h>

## Description

Represents a named view as seen in the browser.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [apply](NamedView_apply.htm) | This updates the active viewport to use the camera associated with this named view. |
| [classType](NamedView_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](NamedView_deleteMe.htm) | Deletes this named view. This method will fail for any of the four standard named views. This can be determined by checking to see if the isBuiltIn property is true. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [camera](NamedView_camera.htm) | Gets and sets the camera associated with this named view. This property acts as read-only for the four standard named views. This can be determined by checking to see if the isBuiltIn property is true. |
| [isBuiltIn](NamedView_isBuiltIn.htm) | Indicates if this named view is one of the four standard named views ("TOP", "FRONT", "RIGHT", and "HOME"). There is limited functionality with the four standard named views. |
| [isValid](NamedView_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](NamedView_name.htm) | Gets and sets the name of this named view. This property acts as read-only for the four standard named views. This can be determined by checking to see if the isBuiltIn property is true. |
| [objectType](NamedView_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentProduct](NamedView_parentProduct.htm) | Returns the parent product of this named view. |

## Accessed From

[NamedViews.add](NamedViews_add.htm), [NamedViews.frontNamedView](NamedViews_frontNamedView.htm), [NamedViews.homeNamedView](NamedViews_homeNamedView.htm), [NamedViews.item](NamedViews_item.htm), [NamedViews.itemByName](NamedViews_itemByName.htm), [NamedViews.rightNamedView](NamedViews_rightNamedView.htm), [NamedViews.topNamedView](NamedViews_topNamedView.htm)

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |