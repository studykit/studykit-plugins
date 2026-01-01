# UserInterface.toolbars Property

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

Gets a collection that provides access to the toolbars. This includes the left and right QAT, and the Navbar.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterface\_var" is a variable referencing a UserInterface object. |

"userInterface\_var" is a variable referencing a UserInterface object. ```` ``` #include <Core/UserInterface/UserInterface.h>  // Get the value of the property. Ptr<Toolbars> propertyValue = userInterface_var->toolbars(); ``` ```` |

## Property Value

This is a read only property whose value is a [Toolbars](Toolbars.htm).

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