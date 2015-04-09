% Clean up.
clear all;
close all;
clc;

% Load task data.
load('train_data.mat');
load('test_data.mat');

%% Preprocess number of chars per word.
train_n_chars_per_word = double(train_n_chars)./double(train_wordcount_data);
test_n_chars_per_word = double(test_n_chars)./double(test_wordcount_data);

%% Neural Network
n_hidden_units = [1];

% Preallocate for speed.
net_test_result = zeros(length(n_hidden_units), 1);
% Test various numbers of hidden units.
for i_hidden_units = 1:length(n_hidden_units)
   n_hidden_units(i_hidden_units)
   net = feedforwardnet(n_hidden_units(i_hidden_units));
   net = train(net, [double(train_wordcount_data); train_n_chars_per_word; double(train_contains_quantity); double(train_top_wordcounts)], double(train_task_labels));
   
   % Error Validation
   net_test_result = net([double(test_wordcount_data); test_n_chars_per_word; double(test_contains_quantity); double(test_top_wordcounts)]);
   res = net_test_result;
   
   % Segment based on trained percentiles.
   percentile_cutoff = (1 - sum(train_task_labels)/length(train_task_labels))*100;
   th = prctile(res, percentile_cutoff);
   res(res>=th)=1;
   res(res<th)=0;
   
    n_true_positives(i_hidden_units) = 0;
    n_false_positives(i_hidden_units) = 0;
    n_true_negatives(i_hidden_units) = 0;
    n_false_negatives(i_hidden_units) = 0;
    true_positive_tasks = [];
    false_positive_tasks = [];
    true_negative_tasks = [];
    false_negative_tasks = [];
    for ii=1:length(res)
        if test_task_labels(ii) == 1 && train_task_labels(ii) == 1
            n_true_positives(i_hidden_units) = n_true_positives(i_hidden_units) + 1; 
           true_positive_tasks = [true_positive_tasks; test_task_descriptions(ii,:)];
        end
        if test_task_labels(ii) == 0 && res(ii) == 1
            n_false_positives(i_hidden_units) = n_false_positives(i_hidden_units) + 1;
            false_positive_tasks = [false_positive_tasks; test_task_descriptions(ii,:)];
        end
        if test_task_labels(ii) == 0 && res(ii) == 0
            n_true_negatives(i_hidden_units) = n_true_negatives(i_hidden_units) + 1;
            true_negative_tasks = [true_negative_tasks; test_task_descriptions(ii,:)];
        end
        if test_task_labels(ii) == 1 && res(ii) == 0
            n_false_negatives(i_hidden_units) = n_false_negatives(i_hidden_units) + 1;
            false_negative_tasks = [false_negative_tasks; test_task_descriptions(ii,:)];
        end
    end
    success_rate(i_hidden_units) = (n_true_positives(i_hidden_units) + n_true_negatives(i_hidden_units)) / length(test_task_labels);
    success_rate_negatives(i_hidden_units) = n_true_negatives / (n_true_negatives + n_false_negatives);
    success_rate_positives(i_hidden_units) = n_true_positives / (n_true_positives + n_false_positives);
    
    save result.mat
end

% Plot negative success rate
plot(n_hidden_units, success_rate_negatives)
xlabel('# of Hidden Units');
ylabel('Success Rate');
title('Success Rate of Predicting Incomplete Tasks');

figure;

% Plot negative success rate
plot(n_hidden_units, success_rate_positives)
xlabel('# of Hidden Units');
ylabel('Success Rate');
title('Success Rate of Predicting Complete Tasks');

figure;

% Plot overall success rate
plot(n_hidden_units, success_rate)
xlabel('# of Hidden Units');
ylabel('Success Rate');
title('Success Rate of Predicting All Tasks');