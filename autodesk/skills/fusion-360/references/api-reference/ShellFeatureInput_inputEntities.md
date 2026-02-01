# ShellFeatureInput.inputEntities Property

Parent Object: [ShellFeatureInput](ShellFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeatureInput.h>

## Description

Gets and sets the input faces/bodies. If IsTangentChain is true, all the faces that are tangentially connected to the input faces (if any) will also be included. Fails if any faces are input, and the owning bodies of the faces are also input.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeatureInput\_var" is a variable referencing a ShellFeatureInput object. |

"shellFeatureInput\_var" is a variable referencing a ShellFeatureInput object. ```` ``` #include <Fusion/Features/ShellFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = shellFeatureInput_var->inputEntities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = shellFeatureInput_var->inputEntities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |