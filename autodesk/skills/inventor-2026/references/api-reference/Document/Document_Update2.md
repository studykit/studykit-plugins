# Document.Update2 Method

Parent Object: [Document](../Document/Document.md)

## Description

Method that performs compute operations on all of the entities within this Document's scope that may be out of date with respect to their driving entities.

## Remarks

The method should return False if any error is encountered during the update process (regardless of the IgnoreErrors argument). The IgnoreErrors argument just specifies whether to stop and return as soon as the first error is encountered or to continue on and finish the update by accepting the errors. A failed re-compute must be handled in a similar manner as through the UI, because typically such failures require some intuitive interpretation. This means examining the model. In API terms, this involves iterating through the parts and features, checking their HealthStatus values. A useful technique is to use SetEndOfPart to help confirm whether an error disappears when part of the model is excluded.

## Syntax

Document.**Update2**( [***AcceptErrorsAndContinue***] As Boolean ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AcceptErrorsAndContinue | Boolean | Optional argument that specifies if errors should be ignored and the update completed or if the update should be aborted if an error occurs. If the IgnoreErrors argument is set to True, errors are skipped and the update process continues. If IgnoreErrors is set to False, the method returns as soon as the first error is encountered. |

## Version

Introduced in version 10
