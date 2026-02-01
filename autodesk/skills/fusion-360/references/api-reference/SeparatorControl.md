# SeparatorControl Object

Derived from: [ToolbarControl](ToolbarControl.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SeparatorControl.h>

## Description

Represents a separator within a panel, toolbar, or drop-down control.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SeparatorControl_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](SeparatorControl_deleteMe.htm) | Deletes the ToolbarControl |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [id](SeparatorControl_id.htm) | Gets the unique ID of this control. The ID is unique with respect to the other controls within the same panel, toolbar, or drop-down control. |
| [index](SeparatorControl_index.htm) | Gets the position of this control within the list of controls within the panel, toolbar, or drop-down control. |
| [isValid](SeparatorControl_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](SeparatorControl_isVisible.htm) | Gets or sets if this control is currently visible. |
| [objectType](SeparatorControl_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](SeparatorControl_parent.htm) | Gets the Parent object. When associated with a toolbar (right or left QAT or the NavBar) this returns the parent Toolbar object. When associated with a panel it returns the parent ToolbarPanel object. When associated with a control (DropDownControl) it returns the parent control. |

## Accessed From

[ToolbarControls.addSeparator](ToolbarControls_addSeparator.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write user interface to a file API Sample](WriteUserInterfaceToFile_Sample.htm) | Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic [User-Interface Customization with Fusion's API](UserInterface_UM.htm) |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |