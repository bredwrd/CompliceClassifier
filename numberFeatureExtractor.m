% author: Alisa Schaefer


function [numberFeature] = numberFeatureExtractor(taskDescrip)
    
    %% Look for numbers in the task descriptions
    numberFeature = ones(1,size(taskDescrip,1));
    for task = 1:size(taskDescrip,1)
        indexStartTask = strfind(taskDescrip(task,:),')');
        shortTask = taskDescrip(task,indexStartTask(1)+1:end);
        nums = regexp(shortTask,'\d+','match');
        
        if (~isempty(nums))
            numberFeature(task) = true;
        else
            numberFeature(task) = false;
        end
    end
    
    %% Count the appearance of the 200 most common words
    %commonWords = mostCommonWords(taskDescrip, 200);
end