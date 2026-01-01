# FileDialog.initialFilename Property

Parent Object: [FileDialog](FileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FileDialog.h>

## Description

Gets or sets the initial filename displayed when the dialog is first displayed. When a new FileDialog object is created this defaults to an empty string so no initial filename is specified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fileDialog\_var" is a variable referencing a FileDialog object.  ```` ``` # Get the value of the property. propertyValue = fileDialog_var.initialFilename  # Set the value of the property. fileDialog_var.initialFilename = propertyValue ``` ```` |

"fileDialog\_var" is a variable referencing a FileDialog object. ```` ``` #include <Core/UserInterface/FileDialog.h>  // Get the value of the property. string propertyValue = fileDialog_var->initialFilename();  // Set the value of the property, where value_var is a string. bool returnValue = fileDialog_var->initialFilename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |