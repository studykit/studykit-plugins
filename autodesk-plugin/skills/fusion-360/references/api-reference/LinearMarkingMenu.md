# LinearMarkingMenu Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/LinearMarkingMenu.h>

## Description

Represents the linear marking menu which is the vertical menu that's displayed when the user right-clicks within Fusion. This supports customizing the contents of the context menu.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](LinearMarkingMenu_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [clear](LinearMarkingMenu_clear.htm) | Completely clears the contents of the context menu. If left in this state, the context menu will not be displayed. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [controls](LinearMarkingMenu_controls.htm) | Return the collection of top-level controls in the context menu. It's possible to have drop-down controls (fly-outs) that provide access to additional controls. You can remove and add controls to customize the contents of the context menu. |
| [isValid](LinearMarkingMenu_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](LinearMarkingMenu_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[MarkingMenuEventArgs.linearMarkingMenu](MarkingMenuEventArgs_linearMarkingMenu.htm)

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |