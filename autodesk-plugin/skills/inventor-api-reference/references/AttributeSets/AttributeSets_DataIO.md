# AttributeSets.DataIO Property

Parent Object: [AttributeSets](../AttributeSets/AttributeSets.md)

## Description

Property that returns the object that allows you to write the contents of all of the AttributeSets attached to object as XML. The DataIO object returned supports the WriteDataToFile method with the format "XML." The AttributeSet names are used as the tag names in the XML data. Because of this, the names must be valid XML tag names. This means they must begin with a letter and can contain the following characters '\_', '-', '.'. Spaces are not allowed.

## Syntax

AttributeSets.**DataIO**() As [DataIO](../DataIO/DataIO.md)

## Property Value

This is a read only property whose value is a [DataIO](../DataIO/DataIO.md).

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |