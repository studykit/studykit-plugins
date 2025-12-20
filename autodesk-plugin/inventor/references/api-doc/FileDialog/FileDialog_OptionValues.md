# FileDialog.OptionValues Property

Parent Object: [FileDialog](../FileDialog/FileDialog.md)

## Description

Read-only property that returns the settings the user specified in the options dialog when a file type known to Inventor was selected. This includes the standard Inventor types (.ipt, .iam, .idw, etc.) and also any files types supported by any translator add-ins. In the case where it’s an unknown type (i.e. .txt, .xml), or if no options were specified this property will return Nothing.The NameValueMap that’s returned can be used directly as the NameValueMap for the corresponding translator add-in.

## Syntax

FileDialog.**OptionValues**() As [NameValueMap](../NameValueMap/NameValueMap.md)

## Property Value

This is a read only property whose value is a [NameValueMap](../NameValueMap/NameValueMap.md).

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |