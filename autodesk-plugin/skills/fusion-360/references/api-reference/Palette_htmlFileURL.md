# Palette.htmlFileURL Property

Parent Object: [Palette](Palette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palette.h>

## Description

Gets and sets the URL to the HTML file that will be displayed in the palette. This can be a local file or a URL on the web where the HTML will be read. To avoid reading a file, this can also be the full HTML definition as a string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"palette\_var" is a variable referencing a Palette object.  ```` ``` # Get the value of the property. propertyValue = palette_var.htmlFileURL  # Set the value of the property. palette_var.htmlFileURL = propertyValue ``` ```` |

"palette\_var" is a variable referencing a Palette object. ```` ``` #include <Core/UserInterface/Palette.h>  // Get the value of the property. string propertyValue = palette_var->htmlFileURL();  // Set the value of the property, where value_var is a string. bool returnValue = palette_var->htmlFileURL(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |