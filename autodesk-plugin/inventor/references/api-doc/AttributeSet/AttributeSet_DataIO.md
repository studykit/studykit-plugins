# AttributeSet.DataIO Property

Parent Object: [AttributeSet](../AttributeSet/AttributeSet.md)

## Description

Property that returns the object that allows you to write the contents of the AttributeSet as XML. The DataIO object returned supports the WriteDataToFile method with the format "XML." The AttributeSet name is used as a tag name in the XML data. Because of this, the name must be a valid XML tag name. This means it must begin with a letter and can contain the following characters '\_', '-', '.'. Spaces are not allowed.

## Syntax

AttributeSet.**DataIO**() As [DataIO](../DataIO/DataIO.md)

## Property Value

This is a read only property whose value is a [DataIO](../DataIO/DataIO.md).

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |