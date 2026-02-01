# Machine.postURL Property

Parent Object: [Machine](Machine.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/Machine.h>

## Description

Gets or sets the URL of the post assigned to the machine.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machine\_var" is a variable referencing a Machine object. |

"machine\_var" is a variable referencing a Machine object. ```` ``` #include <Cam/Machine/Machine.h>  // Get the value of the property. Ptr<URL> propertyValue = machine_var->postURL();  // Set the value of the property, where value_var is a URL. bool returnValue = machine_var->postURL(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [URL](URL.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |