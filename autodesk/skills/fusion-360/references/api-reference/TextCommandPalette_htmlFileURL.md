# TextCommandPalette.htmlFileURL Property

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

Gets and sets the URL to the HTML file that will be displayed in the palette. This can be a local file or a URL on the web where the HTML will be read. To avoid reading a file, this can also be the full HTML definition as a string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textCommandPalette\_var" is a variable referencing a TextCommandPalette object.  ```` ``` # Get the value of the property. propertyValue = textCommandPalette_var.htmlFileURL  # Set the value of the property. textCommandPalette_var.htmlFileURL = propertyValue ``` ```` |

"textCommandPalette\_var" is a variable referencing a TextCommandPalette object. ```` ``` #include <Core/UserInterface/TextCommandPalette.h>  // Get the value of the property. string propertyValue = textCommandPalette_var->htmlFileURL();  // Set the value of the property, where value_var is a string. bool returnValue = textCommandPalette_var->htmlFileURL(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |