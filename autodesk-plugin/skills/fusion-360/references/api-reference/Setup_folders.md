# Setup.folders Property

Parent Object: [Setup](Setup.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/Setup.h>

## Description

Returns the Folders collection that provides access to existing folders in this setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setup\_var" is a variable referencing a Setup object. |

"setup\_var" is a variable referencing a Setup object. ```` ``` #include <Cam/CAM/Setup.h>  // Get the value of the property. Ptr<CAMFolders> propertyValue = setup_var->folders(); ``` ```` |

## Property Value

This is a read only property whose value is a [CAMFolders](CAMFolders.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |