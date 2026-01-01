# ToolbarControl Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarControl.h>

## Description

The base class for all toolbar controls.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ToolbarControl_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](ToolbarControl_deleteMe.htm) | Deletes the ToolbarControl |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [id](ToolbarControl_id.htm) | Gets the unique ID of this control. The ID is unique with respect to the other controls within the same panel, toolbar, or drop-down control. |
| [index](ToolbarControl_index.htm) | Gets the position of this control within the list of controls within the panel, toolbar, or drop-down control. |
| [isValid](ToolbarControl_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](ToolbarControl_isVisible.htm) | Gets or sets if this control is currently visible. |
| [objectType](ToolbarControl_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](ToolbarControl_parent.htm) | Gets the Parent object. When associated with a toolbar (right or left QAT or the NavBar) this returns the parent Toolbar object. When associated with a panel it returns the parent ToolbarPanel object. When associated with a control (DropDownControl) it returns the parent control. |

## Accessed From

[ToolbarControlList.item](ToolbarControlList_item.htm), [ToolbarControlList.itemById](ToolbarControlList_itemById.htm), [ToolbarControls.item](ToolbarControls_item.htm), [ToolbarControls.itemById](ToolbarControls_itemById.htm)

## Derived Classes

[CommandControl](CommandControl.htm), [DropDownControl](DropDownControl.htm), [SeparatorControl](SeparatorControl.htm), [SplitButtonControl](SplitButtonControl.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Customizing the UI using the API Sample](UICustomizationSample_Sample.htm) | Demonstrates how to work with tabs, panels, and command in the user interface. The full source for [C++](../ExtraFiles/UICustomizationSampleCPP.zip) and [Python](../ExtraFiles/UICustomizationSamplePython.zip) samples can be downloaded. This is especially useful for getting the resource files. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |