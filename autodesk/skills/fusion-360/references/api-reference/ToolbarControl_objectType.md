# ToolbarControl.objectType Property

Parent Object: [ToolbarControl](ToolbarControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarControl.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarControl\_var" is a variable referencing a ToolbarControl object.  ```` ``` # Get the value of the property. propertyValue = toolbarControl_var.objectType ``` ```` |

"toolbarControl\_var" is a variable referencing a ToolbarControl object. ```` ``` #include <Core/UserInterface/ToolbarControl.h>  // Get the value of the property. string propertyValue = toolbarControl_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

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