# FolderDialog.initialDirectory Property

Parent Object: [FolderDialog](FolderDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FolderDialog.h>

## Description

Gets or sets the initial directory displayed by the file dialog box.

## Syntax

* [Python](#Python)
* [C++](#C++)

"folderDialog\_var" is a variable referencing a FolderDialog object. |

"folderDialog\_var" is a variable referencing a FolderDialog object. ```` ``` #include <Core/UserInterface/FolderDialog.h>  // Get the value of the property. string propertyValue = folderDialog_var->initialDirectory();  // Set the value of the property, where value_var is a string. bool returnValue = folderDialog_var->initialDirectory(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |