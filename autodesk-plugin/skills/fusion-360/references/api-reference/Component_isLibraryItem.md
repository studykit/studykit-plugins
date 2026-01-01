# Component.isLibraryItem Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Gets whether the component was created from a fasteners library item."

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. boolean propertyValue = component_var->isLibraryItem(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Library Item API Sample](LibraryItemSample_Sample.htm) | Demonstrates how to examine library items using the API.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the existing default code. The script will search for and record all components and library items in the current project. They are displayed in a dialog when the script has finished. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |