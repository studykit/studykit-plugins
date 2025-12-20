# AssemblyDocument.Update2 Method

Parent Object: [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md)

## Description

Method that performs compute operations on all of the entities within this Document's scope that may be out of date with respect to their driving entities.

## Syntax

AssemblyDocument.**Update2**( [***AcceptErrorsAndContinue***] As Boolean ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AcceptErrorsAndContinue | Boolean | Optional argument that specifies if errors should be ignored and the update completed or if the update should be aborted if an error occurs. If the IgnoreErrors argument is set to True, errors are skipped and the update process continues. If IgnoreErrors is set to False, the method returns as soon as the first error is encountered. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |