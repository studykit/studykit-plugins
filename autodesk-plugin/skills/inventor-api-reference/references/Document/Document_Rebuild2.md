# Document.Rebuild2 Method

Parent Object: [Document](../Document/Document.md)

## Description

Method that performs compute operations on all of the entities within this Document's scope as if all of the driving entities had been 'dirtied'.

## Remarks

The method returns False if any errors are encountered during the rebuild. **Please Note:** The rebuild and Rebuild2 methods are not applicable on DrawingDocument and PresentationDocument objects, which do not support rebuilding.

## Syntax

Document.**Rebuild2**( [***AcceptErrorsAndContinue***] As Boolean ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AcceptErrorsAndContinue | Boolean | Optional argument that specifies if errors should be ignored and the rebuild completed or if the rebuild should be aborted if an error occurs. If the IgnoreErrors argument is set to True, errors are skipped and the rebuild process continues. If IgnoreErrors is set to False, the method returns as soon as the first error is encountered. |

## Version

Introduced in version 2008
