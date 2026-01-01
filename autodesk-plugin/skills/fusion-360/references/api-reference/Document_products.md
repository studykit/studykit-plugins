# Document.products Property

Parent Object: [Document](Document.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Document.h>

## Description

Returns the products associated with this document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"document\_var" is a variable referencing a Document object. |

"document\_var" is a variable referencing a Document object. ```` ``` #include <Core/Application/Document.h>  // Get the value of the property. Ptr<Products> propertyValue = document_var->products(); ``` ```` |

## Property Value

This is a read only property whose value is a [Products](Products.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Generate Setup Sheets API Sample](GenerateSetupSheets_Sample_Sample.htm) | Demonstrates generating the setup sheets for an existing toolpath.. |
| [Generate Toolpaths API Sample](GenerateToolpaths_Sample_Sample.htm) | Demonstrates generating the toolpaths in the active document. |
| [Post Toolpaths API Sample](PostToolpaths_Sample_Sample.htm) | Demonstrates posting toolpaths in the active document. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |